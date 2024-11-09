function generateImage() {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    
    // Очистка холста
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Генерация случайного цвета
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);

    // Генерация случайного размера и позиции
    const radius = Math.floor(Math.random() * 100) + 20;
    const x = Math.floor(Math.random() * (canvas.width - radius * 2)) + radius;
    const y = Math.floor(Math.random() * (canvas.height - radius * 2)) + radius;

    // Рисуем круг с случайным цветом и размером
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2 * Math.PI);
    ctx.fillStyle = randomColor;
    ctx.fill();
}
