var tags = [
    'The writings of a Software Engineer and Chief Executive.',
    'The writings of a Software Engineer.',
    'The writings of a Chief Executive.',
    'The writings of a Programmer.',
    'The blog of a guy that writes code.',
    'Do you think pigeons have feelings?',
    'This site is open source!',
    'Built in Django!',
    'Built in Django &amp; Powered by FreeBSD!',
    'Built with Love!',
    'Built with <span class="text-red-800"><i class="fas fa-heart"></i></span>',
    'Built in the USA!',
    '"Arguing that you don\'t care about the right to privacy because you have nothing to hide, is no different than saying you don\'t care about free speech because you have nothing to say." - Edward Snowden',
    'Trust, but verify',
    '"All our dreams can come true, if we have the courage to pursue them." - Walt Disney',
    '"Someone is sitting in the shade today because someone planted a tree a long time ago." - Warren Buffett',
    '"If you can\'t explain it simply, you don\'t understand it well enough." - Albert Einstein',
    'I love code',
    'I love you <span class="text-red-800"><i class="fas fa-heart"></i></span>',
    'Thanks for visiting my site! :)',
    '"The way to get started is to quit talking and begin doing." - Walt Disney',
    '"Life is what happens when you\'re busy making other plans." - John Lennon',
    '"Tell me and I forget. Teach me and I remember. Involve me and I learn." - Benjamin Franklin',
    '"Never let the fear of striking out keep you from playing the game." - Babe Ruth',
    '"The way to get started is to quit talking and begin doing." - Walt Disney'
];

var headings = [
    'Blog',
    'TRDWLL Blog',
    'Gamedev Blog',
    'Blawg',
    'Russ\' Blog'
];

$(document).ready(function() {
    $('.year').append(new Date().getFullYear());

    var tag = tags[Math.floor(Math.random() * tags.length)];
    $('#home-tagline').html(tag);
    var heading = headings[Math.floor(Math.random() * headings.length)];
    $('#home-title').html(heading);

    const menuBtn = document.getElementById('menu-btn');
    const menuNav = document.getElementById('menu-nav');

    menuBtn.addEventListener('click', (e) => {
        e.preventDefault();
        menuNav.classList.toggle('hidden');
    });
});
