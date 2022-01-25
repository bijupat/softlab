(function(){
    const eid = document.querySelector('#eid').innerHTML;
    //document.querySelector('#addtestinput').style.display = "none";
    document.querySelector('#addeditdiscout').style.display = "none";
 
    

   

    //console.log(eid);
    //console.log(document.querySelector('#addpayment'));
    //document.querySelector('#addpayment').addEventListener("click", function(event){
       // event.preventDefault();
       // alert("add Payment clicked!");        
    //});



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

    /*
    //display element for add test when  add test button clicked
    document.querySelector('#addtestbtn').addEventListener("click", function(event){
        event.preventDefault();
        //displa input form
        document.querySelector('#addtestinput').style.display = "block";
        //hide addtest button
        document.querySelector('#addtestbtn').style.display = "none";


        //alert("add test clicked!");
    });
    */
    

    // on click of delete post fetch done to /deletetest/ route with data as json
    document.querySelectorAll('.deletetest').forEach(function(element){            

            element.addEventListener("click", function(event){
            //to prevent submitting form
            event.preventDefault();
            testname = this.previousElementSibling.innerHTML;
            testprice = this.nextElementSibling.innerHTML;
            previous_total = document.querySelector('#totalamount').innerHTML
            previous_due = document.querySelector('#due').innerHTML
            //console.log(previous_due);
            //console.log(testname);
            //console.log(typeof(testname));
            //console.log(this.parentElement.innerHTML);
            // delete li element which is parent to this delete button
            this.parentElement.remove();
            //console.log(document.querySelector('#totalamount').innerHTML)
            //update new total to html  
            document.querySelector('#totalamount').innerHTML=previous_total - testprice
             //update new due to HTML
            document.querySelector('#due').innerHTML=previous_due - testprice
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
    
    
    document.querySelector('#addtestdropbtn').addEventListener("click", function(event){
        document.getElementById("myDropdown").classList.toggle("show");


    });

    document.querySelector('#myInput').addEventListener("keyup", function(event){
        //alert("my input clicked");
        var input, filter, ul, li, a, i;
        input = document.getElementById("myInput");
        filter = input.value.toUpperCase();
        //alert(filter);
        div = document.getElementById("myDropdown");
        a = div.getElementsByTagName("a");
        for (i = 0; i < a.length; i++) {
          txtValue = a[i].textContent || a[i].innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
          } else {
            a[i].style.display = "none";
          }
        }

    });

    
})()

