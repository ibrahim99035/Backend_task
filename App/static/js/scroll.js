let upSpan = document.querySelector('.up')
window.onscroll = function(){
    console.log(this.scrollY);
    if(this.scrollY >= 1000){
        upSpan.classList.add('show');
    }
    else{
        upSpan.classList.remove('show');
    }
};

upSpan.addEventListener('click', function(){
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});