$(function () {
    $("select").select2();
  });


(function(){   
    document.querySelector('#tablediv').style.display = "none";
    document.querySelector('#addtest').addEventListener("click", function(event){
        event.preventDefault();
        //console.log(event.target);
        let element = document.querySelector('#test_select')
        let selected_option = element.options[element.selectedIndex]
        let netprice = parseInt(selected_option.getAttribute("data-price"));
        let regprice = parseInt (selected_option.getAttribute("data-aapm"));
        let disc = parseInt(regprice- netprice);
        console.log(disc)
        let test = selected_option.value;
        //let first_option = element.options[0];

        //console.log(test, price);
        element = document.querySelector("#pricetablebody");
        let tr = document.createElement("tr");
        tr.innerHTML = `<td>${test}</td>
                        <td>${regprice}</td>
                        <td>${disc}</td>
                        <td>${netprice}</td>`;
        element.append(tr);
        totalreg = parseInt(document.querySelector("#totalreg").innerHTML);
        totalreg = totalreg + regprice;
        document.querySelector("#totalreg").innerHTML = totalreg;

        totaldisc = parseInt(document.querySelector("#totaldisc").innerHTML);
        totaldisc = totaldisc + disc;
        document.querySelector("#totaldisc").innerHTML = totaldisc;

        totalnet = parseInt(document.querySelector("#totalnet").innerHTML);
        totalnet = totalnet + netprice;
        document.querySelector("#totalnet").innerHTML = totalnet;
        
        document.querySelector('#tablediv').style.display = "block";

        //hide the selected option         
        selected_option.remove();

    });

    
    
    

    
})()



/*
document.querySelector('#resetlist').addEventListener("click",function(event){
      event.preventDefault();
      htmltext = `<table class="table table-hover">
                  <thead>
                    <tr>
                      <th scope="col">Test</th>
                      <th scopce="col">Reg Price</th>
                      <th scope="col">Discount</th>
                      <th scope="col">Net Price</th>
                    </tr>
                  </thead>
                  <tbody id = "pricetablebody">
                  </tbody>
                  <tfoot>
                    <tr>
                      <td>Total</td>
                      <td id ="totalreg">0</td>
                      <td id="totaldisc">0</td>            
                      <td id="totalnet">0</td>
                    </tr>
                  </tfoot>
                </table>`
      document.querySelector('#tablediv').innerHTML= htmltext;
      document.querySelector('#tablediv').style.display = "none";
    });


el = document.getElementById('test_select');
    dl = document.getElementById('testlist');
    function AddValue(el, dl){
        if(el.value.trim() != ''){
          var opSelected = dl.querySelector(`[value="${el.value}"]`);
          var option = document.createElement("option");
          option.value = opSelected.value;
          option.text = opSelected.getAttribute('label');
          document.getElementById('Colors').appendChild(option);
        }
      }
    

*/