(function(){
    const eid = document.querySelector('#eid').innerHTML;
    console.log(eid);
    //console.log(document.querySelector('#addpayment'));
    document.querySelector('#addpayment').addEventListener("click", function(event){
        event.preventDefault();
        alert("add Payment clicked!");        
    });



    document.querySelector('#addeditdisc').addEventListener("click", function(event){
        event.preventDefault();
        alert("add edit Discount clicked!");   
    });

    


    document.querySelectorAll('.deletetest').forEach(function(element){

            

            element.addEventListener("click", function(event){
            //to prevent submitting form
            event.preventDefault();
            testname = this.previousElementSibling.innerHTML;
            //console.log(testname);
            //console.log(typeof(testname));
            //console.log(this.parentElement.innerHTML);
            // delete li element which is parent to this delete button
            alert("Are You sure to delete the test?");   
            this.parentElement.remove();     
            data = { eid: eid, test: testname }
            option = {
                method: 'POST', // *GET, POST, PUT, DELETE, etc.
                headers: {
                    'Content-Type': 'application/json'
                    // 'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: JSON.stringify(data) // body data type must match "Content-Type" header
                };
            fetch('/deletetest/', option);
            });
    });
         
           
})()

