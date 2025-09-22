(function () {
  const ua = navigator.userAgent || '';
  const w = window.innerWidth;
  let device = 'desktop';
  if (w < 600 || /iphone|android.*mobile|windows phone|ipod/i.test(ua)) device = 'mobile';
  else if ((w >= 600 && w < 1024) || /ipad|tablet|kindle|silk|playbook|nexus 7|sm-t|tab/i.test(ua)) device = 'tablet';
  else device = 'desktop';

  const page = {
    desktop: {
      title: 'AdaptiveSite — Ecommerce',
      headline: 'Sell anything. Fast.',
      sub: 'A modern ecommerce layout for desktop shoppers.',
      bullets: ['Product grid', 'Checkout flow', 'Admin dashboard'],
      mock: '🛒 Desktop Ecommerce Mock',
      btnColor: '#2563eb'
    },
    tablet: {
      title: 'AdaptiveSite — Studio',
      headline: 'Create. Showcase. Inspire.',
      sub: 'A clean studio layout tuned for tablets.',
      bullets: ['Gallery', 'Services', 'Contact form'],
      mock: '🎨 Tablet Studio Mock',
      btnColor: '#9333ea'
    },
    mobile: {
      title: 'AdaptiveSite — Chatan App',
      headline: 'Chat with your people.',
      sub: 'Compact chat UI optimized for phones.',
      bullets: ['Recent chats', 'Quick replies', 'Notifications'],
      mock: '💬 Mobile Chat Mock',
      btnColor: '#16a34a'
    }
  };

  const data = page[device] || page.desktop;

  document.getElementById('page-title').textContent = data.title;
  document.getElementById('headline').textContent = data.headline;
  document.getElementById('sub').textContent = data.sub;
  document.getElementById('ua').textContent = ua;
  document.getElementById('detected').textContent = device;
  const bulletsEl = document.getElementById('bullets');
  bulletsEl.innerHTML = '';
  data.bullets.forEach(b => {
    const li = document.createElement('li');
    li.textContent = b;
    bulletsEl.appendChild(li);
  });

  const mockArea = document.getElementById('mockarea');
  mockArea.innerHTML = `<div class="mock ${device}">${data.mock}</div>`;

  const btn = document.getElementById('primary-btn');
  btn.style.backgroundColor = data.btnColor;
})();
