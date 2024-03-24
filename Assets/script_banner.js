// Массив с новыми путями к изображениям
const newImageURLs = [
  "../Media/banner1.svg", // замените на новый путь к первому изображению
];

// Ожидаем загрузки содержимого страницы
document.addEventListener("DOMContentLoaded", function () {
  // Функция для обновления изображений в слайдере
  function updateSliderImages() {
    // Получаем все слайды в слайдере
    const sliderWrapper = document.querySelector(".mySwiper .swiper-wrapper");

    // Очищаем содержимое слайдера перед добавлением новых изображений
    sliderWrapper.innerHTML = "";

    // Проходим по каждому пути к изображению и создаем новый элемент img для каждого
    newImageURLs.forEach((imageURL) => {
      // Создаем новый элемент слайда
      const slide = document.createElement("div");
      slide.classList.add("swiper-slide");

      // Создаем новое изображение
      const img = document.createElement("img");
      img.src = imageURL;
      img.alt = "slide"; // Устанавливаем альтернативный текст

      // Добавляем изображение в слайд
      slide.appendChild(img);

      // Добавляем слайд в родительский элемент слайдера
      sliderWrapper.appendChild(slide);
    });
  }

  // Вызываем функцию обновления изображений
  updateSliderImages();
});
