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
        let price = selected_option.getAttribute("data-price");
        let test = selected_option.value;
        let first_option = element.options[0];

        //console.log(test, price);
        element = document.querySelector("#pricetablebody");
        let tr = document.createElement("tr");
        tr.innerHTML = `<td>${test}</td>
                        <td>${price}</td>`;
        element.append(tr);
        total = document.querySelector("#total").innerHTML;
        total = parseInt(total) + parseInt(price);
        document.querySelector("#total").innerHTML = total;
        document.querySelector('#tablediv').style.display = "block";


    });

    document.querySelector('#resetlist').addEventListener("click",function(event){
      event.preventDefault();
      htmltext = `<table class="table table-hover">
                  <thead>
                    <tr>
                      <th scope="col">Test</th>
                      <th scope="col">Amout</th>
                    </tr>
                  </thead>
                  <tbody id = "pricetablebody">
                  </tbody>
                  <tfoot>
                    <tr>
                      <td>Total</td>
                      <td id="total">0</td>
                    </tr>
                  </tfoot>
                </table>`
      document.querySelector('#tablediv').innerHTML= htmltext;
      document.querySelector('#tablediv').style.display = "none";
    });
    

    
})()



/*



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