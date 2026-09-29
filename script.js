// Project filter: show cards whose data-tags include the selected filter.
const chips = document.querySelectorAll('.chip');
const cards = document.querySelectorAll('#project-grid .card');

chips.forEach((chip) => {
  chip.addEventListener('click', () => {
    const filter = chip.dataset.filter;
    chips.forEach((c) => {
      const on = c === chip;
      c.classList.toggle('active', on);
      c.setAttribute('aria-pressed', String(on));
    });
    cards.forEach((card) => {
      const tags = card.dataset.tags.split(' ');
      card.hidden = !(filter === 'all' || tags.includes(filter));
    });
  });
});
