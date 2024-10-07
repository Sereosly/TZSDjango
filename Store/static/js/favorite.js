// $(document).ready(function() {
//     $('.favorite-button').on('click', function() {
//         const button = $(this);
//         const productId = button.data('product-id');
//
//         $.ajax({
//             url: '/toggle_favorite/' + productId + '/',
//             type: 'POST',
//             data: {
//                 'csrfmiddlewaretoken': '{{ csrf_token }}',  // Обязательно добавьте токен
//             },
//             success: function(data) {
//                 // Изменяем текст кнопки в зависимости от состояния
//                 if (data.is_favorite) {
//                     button.text('Убрать из избранного');
//                 } else {
//                     button.text('В избранное');
//                 }
//             },
//             error: function(xhr, status, error) {
//                 console.error('Ошибка:', error);
//             }
//         });
//     });
// });