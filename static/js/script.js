document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('upload-form');
    const fileInput = document.getElementById('file-input');
    const predictionDiv = document.getElementById('prediction');
    const tarotCardSpan = document.getElementById('tarot-card');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData();
        formData.append('image', fileInput.files[0]);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            tarotCardSpan.textContent = data.card;
            predictionDiv.textContent = data.prediction;
            predictionDiv.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            predictionDiv.textContent = 'Произошла ошибка при получении предсказания. Попробуйте еще раз.';
            predictionDiv.style.display = 'block';
        }
    });
});
