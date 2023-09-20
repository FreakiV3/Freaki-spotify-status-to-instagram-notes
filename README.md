De l'état Spotify aux notes Instagram
Vous aimez partager votre activité Spotify sur Discord ? Vous avez déjà souhaité le faire sur Instagram aussi ? Eh bien, ce programme est fait pour vous.

Installation
Tout d'abord, vous aurez besoin d'une application dev Spotify, créez-en une ici.
<br>Ajoutez http://localhost:1811/callback comme URI de redirection enregistrée

Ensuite, clonez ce projet sur votre machine :

bash
Copy code
git clone https://github.com/ghrlt/spotify-status-to-instagram-notes.git
Accédez au répertoire :

bash
Copy code
cd spotify-status-to-instagram-notes
Installez les packages requis :

Copy code
python3.10 -m pip install -r requirements.txt
Créez un fichier nommé .env.local et ajoutez les informations suivantes (Supprimez les commentaires) :

js
Copy code
// Vous pouvez trouver cela sur la page de votre application Spotify
SPOTIFY_CLIENT_ID=""
SPOTIFY_CLIENT_SECRET=""

// Entrez les identifiants de votre compte Instagram
INSTAGRAM_USERNAME=""
INSTAGRAM_PASSWORD=""
INSTAGRAM_2FA_SEED="" // Remplissez uniquement si vous avez activé la double authentification et que vous souhaitez générer automatiquement le code 2FA
Si vous passez d'un compte à un autre entre les environnements de production et de développement, vous pouvez également utiliser les fichiers .env.production, .env.production.local, .env.development et .env.development.local.

Configuration
Vous pouvez maintenant lancer l'application :

Copy code
python3.10 app.py
On vous demandera d'ouvrir une page Web pour vous authentifier sur Spotify. Si tout se passe bien, la dernière chose que vous devriez voir est :

json
Copy code
{"success": true}
Vous pouvez ensuite fermer la page et revenir sur votre terminal, où vous devriez voir un message de confirmation. Le programme se connectera ensuite à Instagram en utilisant les informations d'identification fournies dans votre ou vos fichiers d'environnement.

Si votre compte est protégé par une double authentification (2FA), mais que vous n'avez pas rempli le champ INSTAGRAM_2FA_SEED, vous devrez entrer un code 2FA.
En cas d'erreur, le programme affichera l'erreur et se terminera.
Fonctionnement
Le programme effectuera une requête à l'API Spotify pour obtenir la chanson en cours de lecture, formater le nom et l'artiste, puis la publier sur vos notes Instagram.
Pour éviter le spamming, le programme attendra ensuite jusqu'à la fin estimée de la chanson. Il répétera ensuite le processus.

Si vous jouez la même chanson encore et encore, le programme ne publiera pas de nouvelle note. Il ne publiera une nouvelle note que si la chanson est différente de celle précédemment jouée.

Résolution des problèmes
Je ne peux pas me connecter à Instagram, il dit "challenge required"
Je ne peux rien y faire, c'est de la faute d'Instagram. Vous devrez résoudre le défi manuellement depuis votre application Instagram.
Si vous rencontrez un problème, veuillez ouvrir un ticket sur ce dépôt, et j'essaierai de vous aider dès que possible.

Contribution
Si vous souhaitez contribuer à ce projet, n'hésitez pas à ouvrir une demande de pull, je serai ravi de l'examiner !
