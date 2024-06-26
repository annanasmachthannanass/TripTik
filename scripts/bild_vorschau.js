document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('bild').addEventListener('change', function(event) {
        var bildDateien = event.target.files;
        var bildVorschauContainer = document.getElementById('bildVorschauContainer');
        var bildVorschauGroß = document.getElementById('bildVorschauGroß');

        bildVorschauContainer.innerHTML = ''; // Vorherige Vorschauen löschen

        Array.from(bildDateien).forEach((bildDatei, index) => {
            var reader = new FileReader();
            reader.onload = function(e) {
                var img = document.createElement('img');
                img.src = e.target.result;
                img.className = 'bildVorschauKlein';

                // Das letzte Bild wird groß angezeigt
                if (index === bildDateien.length - 1) {
                    bildVorschauGroß.src = e.target.result;
                    bildVorschauGroß.style.display = 'block';
                } else {
                    bildVorschauContainer.appendChild(img);
                }
            }
            reader.readAsDataURL(bildDatei);
        });
    });
});
