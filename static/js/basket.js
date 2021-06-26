// Menu Animate 
document.querySelector('.menu').addEventListener('click',()=>{
    document.querySelectorAll('.target').forEach( (item)=>{
        item.classList.toggle('change');
    })
})
// End Of Menu Animate
