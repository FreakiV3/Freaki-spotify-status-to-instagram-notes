import os
import instagrapi
import env

class Client(instagrapi.Client):
    def __init__(self):
        super().__init__()

    def _login(self):
        self.username = env.INSTAGRAM_USERNAME
        self.mfa_code = ''

        self.session_settings_path = f"{env.WORKING_DIRECTORY_PATH}/ig-{self.username}.session"

        # Chargez les paramètres de session s'ils existent
        if os.path.exists(self.session_settings_path):
            self.load_settings(self.session_settings_path)

        # Connectez-vous
        if env.INSTAGRAM_2FA_SEED:
            self.mfa_code = self.totp_generate_code(env.INSTAGRAM_2FA_SEED)
        
        try:
            self.login(env.INSTAGRAM_USERNAME, env.INSTAGRAM_PASSWORD, verification_code=self.mfa_code)
        except instagrapi.exceptions.TwoFactorRequired:
            print("Instagram | 2FA est activé, mais vous n'avez pas fourni de seed 2FA. Veuillez fournir un seed 2FA dans le fichier .env.")
            self.mfa_code = input("Instagram | Veuillez entrer le code 2FA : ")
            self.login(env.INSTAGRAM_USERNAME, env.INSTAGRAM_PASSWORD, verification_code=self.mfa_code)

        self.dump_settings(self.session_settings_path)

        print("Instagram | Connecté avec succès en tant que", self.username)

    def setStatus(self, status: str):
        if len(status) > 60:
            status = status[:57] + "..."
        
        # Utilisez la méthode create_note pour publier le statut
        note = self.create_note(status, audience=0)
        if note:
            print("Instagram | Statut mis à jour avec succès :", status)

if __name__ == "__main__":
    # Créez une instance de votre classe Client et effectuez la connexion
    client = Client()
    client._login()
    
    # Exemple d'utilisation pour définir le statut
    new_status = "Nouveau statut Instagram !"
    client.setStatus(new_status)