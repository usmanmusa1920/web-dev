bar = document.getElementById('bar').display.style.cssText = 'display:block'
main = document.getElementById('main').display.style.cssText = 'display:block'
foot = document.getElementById('foot').display.style.cssText = 'display:block'
arrowup = document.getElementById('arrowup').display.style.cssText = 'display:block'
arrowdown = document.getElementById('arrowdown').display.style.cssText = 'display:block'

function bardown(){
  bar.style.cssText = 'display:block'
  foot.style.cssText = 'display:none'
  main.style.cssText = 'display:none'
  arrowup.style.display = 'block'
  arrowdown.style.display = 'none'
}

function barup(){
  bar.style.display = 'none'
  foot.style.cssText = 'display:block'
  main.style.cssText = 'display:block'
  arrowup.style.display = 'none'
  arrowdown.style.display = 'block'
}
