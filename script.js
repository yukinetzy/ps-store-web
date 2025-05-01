function showCategory(category) {
  const productsEl = document.getElementById('products');
  productsEl.innerHTML = '';

  fetch('data.json')
    .then(res => res.json())
    .then(data => {
      const products = data[category];
      products.forEach(p => {
        const card = `
          <div class="product-card">
            <h3>${p.name}</h3>
            <p>${p.price}₽</p>
            <a href="${p.ps_link}" target="_blank">🔗 Открыть в PS Store</a>
          </div>
        `;
        productsEl.innerHTML += card;
      });
    });
}
