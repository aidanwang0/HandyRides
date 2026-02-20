function getCookie(c_name) {
  var i, x, y, ARRcookies = document.cookie.split(";");
  for (i = 0; i < ARRcookies.length; i++) {
    x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
    y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
    x = x.replace(/^\s+|\s+$/g, "");
    if (x == c_name) {
      return unescape(y);
    }
  }
  return null;
}

function setCookie(c_name, value, exdays) {
  var exdate = new Date();
  exdate.setDate(exdate.getDate() + exdays);
  var c_value = escape(value) + (exdays == null ? "" : "; expires=" + exdate.toUTCString());
  document.cookie = c_name + "=" + c_value;
}

/**
 * Validates the search form before submit.
 * - If both state and city are blank, do not submit.
 * - If the user searched for "Elon Musk", show popup and do not submit.
 * @returns {boolean} false to prevent submit, true to allow submit
 */
function checkForm() {
  var stateInput = document.getElementById("id_state");
  var cityInput = document.getElementById("id_city");
  var state = stateInput ? stateInput.value.replace(/^\s+|\s+$/g, "") : "";
  var city = cityInput ? cityInput.value.replace(/^\s+|\s+$/g, "") : "";

  if (state === "" && city === "") {
    alert("Please enter at least a state or city to search.");
    return false;
  }

  var stateLower = state.toLowerCase();
  var cityLower = city.toLowerCase();
  if (stateLower === "elon musk" || cityLower === "elon musk") {
    alert("He's not here.");
    return false;
  }

  return true;
}

/**
 * First-visit: set cookie and redirect to splash page.
 * Only redirects when the user has no "visited" cookie (first time).
 */
function handleFirstVisit() {
  if (!getCookie("visited")) {
    setCookie("visited", "1", 365);
    if (window.location.pathname !== "/") {
      window.location.href = "/";
    }
  }
}
