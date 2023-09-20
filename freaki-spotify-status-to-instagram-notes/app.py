import time
import env
import instagram
import spotify

class App:
    def __init__(self):
        self.instagram = instagram.Client()
        self.spotify = spotify.Client()

        self.running = True
        self.lastTrackId = None
        self.lastNoteId = None

    def deleteInstagramNote(
        self,
        onlyIfCreatedByThisScript=False
    ):
        try:
            currentNotes = self.instagram.get_notes()
            if currentNotes:
                currentNote = currentNotes[0]
                if currentNote['id'] == self.lastNoteId or self.lastNoteId is None or onlyIfCreatedByThisScript:
                    self.instagram.delete_note(currentNote['id'])
                    print("Instagram | Note supprimée")
        except Exception as e:
            print("Erreur lors de la suppression de la note Instagram:", e)

    def start(self):
        self.spotify.login()
        self.instagram._login()

        while self.running:
            try:
                currentPlayback = self.spotify.getCurrentPlayback()
                if not currentPlayback:
                    print("Spotify | Pas de lecture / Non disponible")
                    self.wait(10)
                    continue

                if currentPlayback['is_playing'] is False:
                    print("Spotify | Pas de lecture")
                    self.deleteInstagramNote(onlyIfCreatedByThisScript=True)
                    self.wait(60)
                    continue

                if currentPlayback['item']['type'] != 'track':
                    raise Exception(f"Type d'élément non pris en charge : {currentPlayback['item']['type']}")

                track = currentPlayback['item']
                timeLeft = track['duration_ms'] - currentPlayback['progress_ms']
                if timeLeft <= 0:
                    timeLeft = 20

                if track['id'] == self.lastTrackId:
                    self.wait(timeLeft / 1000)
                    continue

                self.lastTrackId = track['id']

                print(f"En train de jouer {track['name']} par {track['artists'][0]['name']}, prochaine chanson dans {timeLeft/1000}s")
                self.instagram.setStatus(
                    f"🎶 {track['name']} par {track['artists'][0]['name']}"
                )

                self.lastNoteId = self.instagram.get_notes()[0]['id']

                self.wait(timeLeft / 1000)
            except Exception as e:
                print("Erreur lors de la mise à jour du statut Instagram :", e)

    def wait(self, seconds):
        print(f"En attente de {seconds} secondes...")
        time.sleep(seconds)

if __name__ == '__main__':
    App().start()
