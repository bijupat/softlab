document.addEventListener("DOMContentLoaded", function () {
  $("#test_select").select2({
    placeholder: "Select test...",
    allowClear: true,
    width: "300px",
  });

  const testSelect = document.getElementById("test_select");
  const resetBtn = document.getElementById("resetlist");
  const priceTableBody = document.getElementById("pricetablebody");
  const tableDiv = document.getElementById("tablediv");
  const totalRegElem = document.getElementById("totalreg");
  const totalDiscElem = document.getElementById("totaldisc");
  const totalNetElem = document.getElementById("totalnet");

  let totalReg = 0;
  let totalDisc = 0;
  let totalNet = 0;

  // Track added tests
  let addedTests = new Set();

  function updateTotals(regPrice, discount, netPrice, add = true) {
    if (add) {
      totalReg += regPrice;
      totalDisc += discount;
      totalNet += netPrice;
    } else {
      totalReg -= regPrice;
      totalDisc -= discount;
      totalNet -= netPrice;
    }
    totalRegElem.textContent = totalReg;
    totalDiscElem.textContent = totalDisc;
    totalNetElem.textContent = totalNet;
  }

  function createRow(test, regPrice, discount, netPrice) {
    const tr = document.createElement("tr");

    tr.innerHTML = `<td class="font-weight-bold text-nowrap">${test}</td>
                    <td class="d-md-table-cell">${regPrice}</td>
                    <td class="d-md-table-cell">${discount}</td>
                    <td class="font-weight-bold">${netPrice}</td>
                    <td class="text-center">
                    <button type="button" class="btn btn-sm btn-danger btn-remove">&times;</button>
                    </td>`;

    tr.querySelector(".btn-remove").addEventListener("click", function () {
      priceTableBody.removeChild(tr);
      updateTotals(regPrice, discount, netPrice, false);
      addedTests.delete(test);

      // Re-enable option in select
      const option = [...testSelect.options].find((opt) => opt.value === test);
      if (option) {
        option.disabled = false;
      }
      $("#test_select").select2("destroy"); // Rebuild select2 to update options
      $("#test_select").select2({
        placeholder: "Select test...",
        allowClear: true,
        width: "300px",
      });

      if (priceTableBody.children.length === 0) {
        tableDiv.style.display = "none";
      }

      // Autofocus search input after removal
      // $(".select2-search__field").focus();
    });

    return tr;
  }
  // document.addEventListener("keydown", function (event) {
  //   const searchInput = document.querySelector(".select2-search__field");
  //   // console.log(event.target);
  //   if (searchInput && document.activeElement !== searchInput) {
  //     console.log("if run");
  //     searchInput.focus();
  //     event.stopPropagation();
  //   }
  // });

  // Add test on selection change
  $("#test_select").on("select2:select", function (e) {
    const selectedOption = e.params.data.element;
    if (!selectedOption) return;
    const test = selectedOption.value;
    if (addedTests.has(test)) {
      alert("Test already added.");
      $("#test_select").val(null).trigger("change");
      // $(".select2-search__field").focus();
      return;
    }

    const optionEl = selectedOption;

    const regPrice = parseInt(optionEl.getAttribute("data-aapm")) || 0;
    const netPrice = parseInt(optionEl.getAttribute("data-price")) || 0;
    const discount = regPrice - netPrice;

    const newRow = createRow(test, regPrice, discount, netPrice);
    priceTableBody.appendChild(newRow);

    updateTotals(regPrice, discount, netPrice, true);
    addedTests.add(test);

    // Disable selected option to prevent re-adding
    optionEl.disabled = true;

    // Refresh select2 to apply option disable
    $("#test_select").select2("destroy");
    $("#test_select").select2({
      placeholder: "Select test...",
      allowClear: true,
      width: "300px",
    });

    // Clear selection
    $("#test_select").val(null).trigger("change");
    // autofocus on select2 search input
    // $(document).on("select2:open", () => {
    //   document.querySelector(".select2-search__field").focus();
    // });
    $(".select2-search__field").focus();

    tableDiv.style.display = "block";
  });

  resetBtn.addEventListener("click", function () {
    priceTableBody.innerHTML = "";
    totalReg = 0;
    totalDisc = 0;
    totalNet = 0;
    totalRegElem.textContent = "0";
    totalDiscElem.textContent = "0";
    totalNetElem.textContent = "0";
    addedTests.clear();

    // Enable all options
    Array.from(testSelect.options).forEach((opt) => {
      opt.disabled = false;
    });

    // Refresh select2 to reflect enabled options
    $("#test_select").select2("destroy");
    $("#test_select").select2({
      placeholder: "Select test...",
      allowClear: true,
      width: "300px",
    });
    // Clear selection
    $("#test_select").val(null).trigger("change");
    // $(document).on("select2:open", () => {
    //   document.querySelector(".select2-search__field").focus();
    // });
    // $(".select2-search__field").focus();
    tableDiv.style.display = "none";
  });
});
