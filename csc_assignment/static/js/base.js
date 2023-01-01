// show menu bar
function showMenu(){
  document.querySelector('.menu').style.display = 'flex'
  document.querySelector('#menu_img').style.display = 'none'
  document.querySelector('.times').style.display = 'flex'
  document.querySelector('.times').style.fontSize = '50px'
  document.querySelector('.times').style.textDecoration = 'none'
}

// hide menu bar
function hideMenu(){
  document.querySelector('.menu').style.display = 'none'
  document.querySelector('#menu_img').style.display = 'block'
  document.querySelector('.times').style.display = 'none'
}

function showDelete(){
  document.querySelector('#hidden_delete').style.display = 'block'
}

function hideDelete(){
  document.querySelector('#hidden_delete').style.display = 'none'
}