document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('question-form');
    const questionInput = document.getElementById('question-input');
    const predictionDiv = document.getElementById('prediction');
    const tarotCardSpan = document.getElementById('tarot-card');
    const predictionTextP = document.getElementById('prediction-text');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData();
        formData.append('question', questionInput.value);

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
            predictionTextP.textContent = data.prediction;
            predictionDiv.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            predictionTextP.textContent = 'Произошла ошибка при получении предсказания. Попробуйте еще раз.';
            predictionDiv.style.display = 'block';
        }
    });
});
