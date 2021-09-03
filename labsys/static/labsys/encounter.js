(function(){
    //console.log(document.querySelector('#addpayment'));
    document.querySelector('#addpayment').addEventListener("click", function(event){
        event.preventDefault();
        alert("add Payment clicked!");        
    });



    document.querySelector('#addeditdisc').addEventListener("click", function(event){
        event.preventDefault();
        alert("add edit Discount clicked!");   
    });



    document.querySelector('#deletetest').addEventListener("click", function(event){
        //event.preventDefault();
        alert("Are You sure to delete the test?");        
        data = { answer: 42 }
        option = {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            headers: {
                'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            credentials: 'same-origin',
            body: JSON.stringify(data) // body data type must match "Content-Type" header
            }
        fetch('/deletetest/', option)
        
    });  
           
})()

