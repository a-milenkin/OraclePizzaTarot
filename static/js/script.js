document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('question-form');
    const questionInput = document.getElementById('question-input');
    const predictionDiv = document.getElementById('prediction');
    const tarotCardsDiv = document.getElementById('tarot-cards');
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
            tarotCardsDiv.innerHTML = '';
            data.cards.forEach(card => {
                const img = document.createElement('img');
                img.src = `/taro_cards_images/${card}`;
                img.alt = '"' + card.split('.')[0].replace(/_/g, ' ') + '"';
                img.className = 'tarot-card-image';
                tarotCardsDiv.appendChild(img);
            });
            predictionTextP.textContent = data.prediction;
            predictionDiv.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            predictionTextP.textContent = 'Произошла ошибка при получении предсказания. Попробуйте еще раз.';
            predictionDiv.style.display = 'block';
        }
    });
});
