(function(){
    const eid = document.querySelector('#eid').innerHTML;
    document.querySelector('#addtestinput').style.display = "none";
    document.querySelector('#addeditdiscout').style.display = "none";

    
    //console.log(eid);
    //console.log(document.querySelector('#addpayment'));
    document.querySelector('#addpayment').addEventListener("click", function(event){
        event.preventDefault();
        alert("add Payment clicked!");        
    });



    document.querySelector('#addeditdisc').addEventListener("click", function(event){
        event.preventDefault(); 
        //alert("add edit Discount clicked!");
        //displa input form
        document.querySelector('#addeditdiscout').style.display = "block";
        //hide addtest button
        document.querySelector('#addeditdisc').style.display = "none";

        
    });
    //enable add discount submit button when addeditdiscountinput selected
    document.getElementById('addeditdiscountinput').addEventListener('input', function () {
        //console.log(document.getElementById('addeditdiscountinput'))
        //alert("keyup  event detected")
        document.querySelector('#addeditdiscountsubmit').disabled = false;
    });


    //display element for add test when  add test button clicked
    document.querySelector('#addtestbtn').addEventListener("click", function(event){
        event.preventDefault();
        //displa input form
        document.querySelector('#addtestinput').style.display = "block";
        //hide addtest button
        document.querySelector('#addtestbtn').style.display = "none";


        //alert("add test clicked!");
    });

    
    
    // on click of delete post fetch done to /deletetest/ route with data as json
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

