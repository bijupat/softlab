// for multiselect in test slection input field 
$(".chosen-select").chosen({
    no_results_text: "Oops, nothing found!"
  });

(function(){
   //hiding new patient divs initially
   document.querySelector('#new_patient').style.display = "none";
   document.querySelector('#old_patient').style.display = "block";

   //hiding name and mobile no search field
   document.querySelector('#name_input').style.display = "none";
   document.querySelector('#mobno_input').style.display = "none";
   document.querySelector('#srchbtn').style.display = "none";
   document.querySelector('#new_pat_btn').style.display = "none";
   document.querySelector('#srch_again').style.display = "none";
   document.querySelector('#srchbtn').disabled=true;
 
  // checking mobile no input value length
 document.querySelector('#mobno').addEventListener("keyup", (e) =>  {
    
    if (e.target.value.length != 10){
      e.target.focus();
      document.querySelector('#srchbtn').disabled=true;
      return ;       
    }
    else {
      document.querySelector('#srchbtn').disabled=false;
    }});   
   



   // checking fname or l name  input value length


   document.querySelector('#fname').addEventListener("keyup", (e) =>  {
    if (e.target.value.length < 3 && document.querySelector('#lname').value.length < 3){
      e.target.focus();
      document.querySelector('#srchbtn').disabled=true;
      return ;       
    }
    else {
      document.querySelector('#srchbtn').disabled=false;
    }});


    document.querySelector('#lname').addEventListener("keyup", (e) =>  {
      if (e.target.value.length < 3 && document.querySelector('#fname').value.length < 3){
        e.target.focus();
        document.querySelector('#srchbtn').disabled=true;
        return ;       
      }
      else {
        document.querySelector('#srchbtn').disabled=false;
      }});

  if (document.querySelector('#error_check')){
    document.querySelector('#error_check').addEventListener("click", function(event){
      event.preventDefault(); 
      //displa new patient div
      document.querySelector('#new_patient').style.display = "block";
      //hide old patient div if displayed already
      document.querySelector('#old_patient').style.display = "none";
      event.target.style.display = "none";        
    });

  }
   

  // on click of new patient button display new patient div
  document.querySelector('#new_pat_btn').addEventListener("click", function(event){
    event.preventDefault(); 
    //displa new patient div
    document.querySelector('#new_patient').style.display = "block";
    //hide old patient div if displayed already
    document.querySelector('#old_patient').style.display = "none";        
  });

  // on click of old patient button display old patient div   
  document.querySelector('#srch_again').addEventListener("click", function(event){
    event.preventDefault();
    // clearing all input fields before new search
    document.querySelector("#mobno").value = ""
    document.querySelector("#fname").value = ""
    document.querySelector("#lname").value = ""
    // disabling search btn
    document.querySelector('#srchbtn').disabled=true;
    //remove all previous seach results
    element = document.querySelector("#SrchRslt").innerHTML = '';
    //hide it self
    event.target.style.display = "none";    
    //displa old patient div
    document.querySelector('#old_patient').style.display = "block";
    document.querySelector('#Srch_by_mobno').style.display = "block";
    document.querySelector('#Srch_by_name').style.display = "block";
    //hide new patient div if displayed already
    document.querySelector('#new_patient').style.display = "none";
    document.querySelector('#mobno_input').style.display = "none";
    document.querySelector('#name_input').style.display = "none";
    document.querySelector('#srchbtn').style.display = "none";
    document.querySelector('#new_pat_btn').style.display = "none";
    event.target.style.display = "none";      
});


  // on click of search by name button display seach by name  div
  document.querySelector('#Srch_by_name').addEventListener("click", function(event){
    event.preventDefault(); 
    //displa seach by name div
    document.querySelector('#name_input').style.display = "block";
    document.querySelector('#srchbtn').style.display = "block";
    document.querySelector('#srch_again').style.display = "block";
    //hide mobinput div if displayed already
    document.querySelector('#mobno_input').style.display = "none";
    document.querySelector('#Srch_by_mobno').style.display = "none";
    event.target.style.display = "none";
  });

  // on click of search by mobileno button display seach by name  div
  document.querySelector('#Srch_by_mobno').addEventListener("click", function(event){
    event.preventDefault(); 
    //display seach by mobno div
    document.querySelector('#mobno_input').style.display = "block";
    document.querySelector('#srchbtn').style.display = "block";
    document.querySelector('#srch_again').style.display = "block";
    //hide mobinput div if displayed already
    document.querySelector('#name_input').style.display = "none";
    document.querySelector('#Srch_by_name').style.display = "none";
    event.target.style.display = "none";
  });

  //fetch from search route
  document.querySelector("#srchbtn").addEventListener("click", (event)=>{
    event.preventDefault();
    // clearing innerHTML FROM LAST SEARCH
    element = document.querySelector("#SrchRslt");
    element.innerHTML = ''    
    fname = document.querySelector("#fname").value
    lname = document.querySelector("#lname").value
    mobno = document.querySelector("#mobno").value
    register = document.querySelector("#register").value
    // checking if any one of the field has 3 charaters
    data = { fname: fname, lname: lname, mobno : mobno  }
    option = {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(data) // body data type must match "Content-Type" header
        };
      fetch('/search/', option)
      .then(response => response.json())
      .then(names => {
        names.forEach(name=>{ 
          let tr = document.createElement("tr");
          // register is value for what to register appointment or encouter?
          tr.innerHTML = `<td class="view-message text-left">${name.patient_id}</td>
                        <td class="view-message text-center "><a href= 'regi_${register}/${name.patient_id}'>${name.fname} ${name.lname} </a> </td>
                        <td class="view-message text-right">${name.mobno}</td>`;
          element.append(tr)
          
        })
      })
      .catch(e => console.error(e))
      //displaying not found add new patient and seach again buttons
      document.querySelector('#new_pat_btn').style.display = "block";
      document.querySelector('#name_input').style.display = "none";
      document.querySelector('#mobno_input').style.display = "none";
      document.querySelector('#srchbtn').style.display = "none";
      });
/* for patient search input option 

        document.querySelector('#searchpatdropdwnbtn').addEventListener("click", function(event){
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
        }); */
})()
