# Spotify status to Instagram notes

Ce programme a été créé par Freakidann pour permettre le partage automatique de votre activité Spotify sur Instagram.

## Installation
Tout d'abord, vous aurez besoin d'une [application Spotify dev](https://developer.spotify.com/documentation/web-api/concepts/apps), que vous pouvez créer [ici](https://developer.spotify.com/dashboard/create).
<br>**Ajoutez `http://localhost:1811/callback` en tant qu'URI de redirection enregistrée** 

Ensuite, clonez ce projet sur votre machine:<br>
`git clone https://github.com/ghrlt/spotify-status-to-instagram-notes.git`

Accédez au répertoire<br>
`cd spotify-status-to-instagram-notes`

Installez les packages requis<br>
`python3.10 -m pip install -r requirements.txt`
<br><br>

Créez un fichier nommé `.env.local` et ajoutez les informations suivantes (Supprimez les commentaires) :
```js
// Vous pouvez trouver ceci sur la page de votre application Spotify
SPOTIFY_CLIENT_ID=""
SPOTIFY_CLIENT_SECRET=""

// Entrez vos informations de compte Instagram
INSTAGRAM_USERNAME=""
INSTAGRAM_PASSWORD=""
INSTAGRAM_2FA_SEED="" // Remplissez uniquement si vous avez activé la 2FA et souhaitez générer automatiquement le code 2FA
```
Si vous passez d'un compte de production à un compte de développement, vous pouvez également utiliser des fichiers .env.production, .env.production.local, .env.development, .env.development.local.

## Configuration
Vous pouvez maintenant démarrer l'application !<br>
`python3.10 app.py`

On vous demandera d'ouvrir une page Web pour vous authentifier sur Spotify. Si tout se passe bien, la dernière chose que vous devriez voir est :
```json
{"success": true}
Vous pouvez alors fermer la page et revenir sur votre terminal, où vous devriez voir un message de confirmation. Ensuite, le programme se connectera à Instagram en utilisant les informations d'identification fournies dans votre/vos fichier(s) d'environnement.

Si votre compte est protégé par la 2FA, mais que vous n'avez pas rempli le champ INSTAGRAM_2FA_SEED, vous devrez fournir un code 2FA.
En cas d'erreur, le programme affichera l'erreur et s'arrêtera.
Fonctionnement
Le programme enverra une requête à l'API Spotify pour obtenir la chanson que vous écoutez actuellement, formatera le nom et l'artiste, puis le publiera dans vos notes Instagram.
Pour éviter le spam, le programme attendra ensuite jusqu'à la fin estimée de la chanson avant de répéter le processus.

Si vous écoutez la même chanson en boucle, le programme ne publiera pas une nouvelle note. Il publiera une nouvelle note uniquement si la chanson est différente de celle précédemment jouée.

Dépannage
Je ne peux pas me connecter à Instagram, il dit "challenge required"
Je ne peux rien y faire, c'est la faute d'Instagram. Vous devrez résoudre le challenge manuellement depuis votre application Instagram.
Si vous rencontrez un problème, veuillez ouvrir un problème sur ce dépôt, et je ferai de mon mieux pour vous aider dans les plus brefs délais.

Contribution
Si vous souhaitez contribuer à ce projet, n'hésitez pas à ouvrir une demande de pull, je serai ravi de l'examiner !
