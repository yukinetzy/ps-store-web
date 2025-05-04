function showCategory(category) {
  const productsEl = document.getElementById('products');
  productsEl.innerHTML = 'Загрузка...';

  fetch('data.json')
    .then(res => res.json())
    .then(data => {
      const products = data[category];
      productsEl.innerHTML = '';

      if (!products || products.length === 0) {
        productsEl.innerHTML = '<p>Нет товаров в этой категории.</p>';
        return;
      }

      products.forEach(p => {
        const card = `
          <div class="product-card">
            <img src="${p.image}" alt="${p.name}">
            <h3>${p.name}</h3>
            <p>${p.price}₽</p>
            <a href="${p.ps_link}" target="_blank">🛒 Купить</a>
          </div>
        `;
        productsEl.innerHTML += card;
      });
    })
    .catch(err => {
      productsEl.innerHTML = '<p>Ошибка загрузки данных.</p>';
      console.error(err);
    });
}
