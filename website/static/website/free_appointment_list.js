document.getElementById("filter-btn").addEventListener("click", function () {
  const dateFilter = document.getElementById("filter-date").value;
  const nameFilter = document.getElementById("filter-name").value.toLowerCase();
  const mobileFilter = document.getElementById("filter-mobile").value;
  const rows = document.querySelectorAll("#appointments-tbody tr");
  function parseAppointmentTime(str) {
    // Example input: "Feb. 21, 2026, 9 a.m."
    const months = {
      Jan: 0,
      Feb: 1,
      Mar: 2,
      Apr: 3,
      May: 4,
      Jun: 5,
      Jul: 6,
      Aug: 7,
      Sep: 8,
      Oct: 9,
      Nov: 10,
      Dec: 11,
    };

    // Remove dots from month abbreviation and split
    const parts = str.replace(".", "").split(/[, ]+/);
    // parts example: ["Feb", "21", "2026", "9", "a.m."]

    const month = months[parts[0].slice(0, 3)];
    const day = parseInt(parts[1], 10);
    const year = parseInt(parts[2], 10);
    let hour = parseInt(parts[3], 10);

    const ampm = parts[4].toLowerCase();
    if (ampm.includes("p") && hour !== 12) hour += 12;
    if (ampm.includes("a") && hour === 12) hour = 0;
    return new Date(year, month, day, hour);
  }
  rows.forEach((row) => {
    const name = row.cells[0].textContent.toLowerCase();
    const mobile = row.cells[1].textContent;
    const appointmentTime = row.cells[2].textContent;
    let show = true;

    if (dateFilter) {
      const apptDate = parseAppointmentTime(appointmentTime);
      const filterDate = new Date(dateFilter);

      if (
        apptDate.getFullYear() !== filterDate.getFullYear() ||
        apptDate.getMonth() !== filterDate.getMonth() ||
        apptDate.getDate() !== filterDate.getDate()
      ) {
        show = false;
      }
    }

    if (nameFilter && !name.includes(nameFilter)) show = false;
    if (mobileFilter && !mobile.includes(mobileFilter)) show = false;

    row.style.display = show ? "" : "none";
  });
});

document.getElementById("clear-btn").addEventListener("click", function () {
  document.getElementById("filter-date").value = "";
  document.getElementById("filter-name").value = "";
  document.getElementById("filter-mobile").value = "";

  const rows = document.querySelectorAll("#appointments-tbody tr");
  rows.forEach((row) => (row.style.display = ""));
});
