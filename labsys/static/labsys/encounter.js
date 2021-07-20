(function(){
    console.log(document.querySelector('#addeditdisc'));
    document.querySelector('#addeditdisc').addEventListener("click", function(event){
        event.preventDefault();
        alert("add edit payment clicked!");
    });
})()