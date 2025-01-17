const open = document.getElementById("openNav");
const close = document.getElementById("closeNav");
const hamburger = document.getElementById("navUl");

open.addEventListener("click", openMenu);
close.addEventListener("click", closeMenu);

function openMenu() {
  hamburger.style.left = "0%";
}

function closeMenu() {
  hamburger.style.left = "-100%";
}

// profile dropdown
const dropdownProfileContent = document.querySelector(".dropdown-profile");
const dropdownProfileButton = document.querySelector("#profileDropdown");

var clickCounter = 0;
dropdownProfileButton.addEventListener("click", () => {
  dropdownProfileContent.style.display = "block";
  clickCounter++;
  if (clickCounter % 2 == 0) {
    dropdownProfileContent.style.display = "none";
  }
});

// cart dropdown
const dropdownCartContent = document.querySelector(".dropdown-cart");
const dropdownCartButton = document.querySelector("#cartDropdown");

var clickCounterCart = 0;
dropdownCartButton.addEventListener("click", () => {
  dropdownCartContent.style.display = "block";
  clickCounterCart++;
  if (clickCounterCart % 2 == 0) {
    dropdownCartContent.style.display = "none";
  }
});

// category dropdown
window.onresize = () => {
  if (window.innerWidth > 1219) {
    const dropdownCategoryContent = document.querySelector(".dropdown-category");
    const dropdownCategoryButton = document.querySelector(".category-li");

    isMouseOutBtn = false;
    isMouseOutContent = false;

    dropdownCategoryButton.addEventListener("mouseover", () => {
      dropdownCategoryContent.style.display = "flex";
    });

    dropdownCategoryButton.addEventListener("mouseout", () => {
      dropdownCategoryContent.style.display = "none";
    });
  }
}

if (window.innerWidth > 1259) {
  const dropdownCategoryContent = document.querySelector(".dropdown-category");
  const dropdownCategoryButton = document.querySelector(".category-li");

  isMouseOutBtn = false;
  isMouseOutContent = false;

  dropdownCategoryButton.addEventListener("mouseover", () => {
    dropdownCategoryContent.style.display = "flex";
  });

  dropdownCategoryButton.addEventListener("mouseout", () => {
    dropdownCategoryContent.style.display = "none";
  });
}

if (window.innerWidth < 1260) {
  const dropdownCategoryContent = document.querySelector(".dropdown-category");
  const dropdownCategoryButton = document.querySelector("#dropdown-chevron");
  const dropdownChevron = document.getElementById('dropdown-chevron')
  let dropdownBtnCounter = 0

  dropdownCategoryButton.addEventListener('click', () => {
    dropdownBtnCounter++;
    if (dropdownBtnCounter % 2 == 0) {
      dropdownCategoryContent.style.display = "none";
      dropdownChevron.style.transform = "rotate(0deg)";
    } else {
      dropdownCategoryContent.style.display = "flex";
      dropdownChevron.style.transform = "rotate(180deg)";
    }
  })
}

// Dropdown columns
const dropdownColBtn = document.getElementById('dropdown-subtopic');
const dropdownColBody = document.getElementById('dropdown-subtopic-body');
const dropdownColChevron = document.getElementById('chevron-down');
const dropdownCategoryContent = document.querySelector(".dropdown-category");
dropdownCategoryContent.style.paddingBottom = "0px";


let dropdownColCounter = 0
dropdownColBtn.addEventListener('click', () => {
  dropdownColCounter++;
  if (dropdownColCounter % 2 == 0) {
    dropdownColBody.style.display = 'none';
    dropdownColChevron.classList.remove("rotate")
    dropdownCategoryContent.style.paddingBottom = "0px";
  } else {
    dropdownColBody.style.display = 'block';
    dropdownColChevron.classList.add("rotate")
  }
})

// detail page tab

function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}


// dropdown category page

// color
const colorBtn = document.getElementById('colors');
const colorBody = document.getElementById('colors-data');
const colorChevron = document.getElementById('color-chevron')

let colorBtnCounter = 1
colorBtn.addEventListener('click', () => {
  colorBtnCounter++;
  if (colorBtnCounter % 2 == 0) {
    colorBody.style.display = 'none';
    colorChevron.classList.remove("rotate")
  } else {
    colorBody.style.display = 'block';
    colorChevron.classList.add("rotate")
  }
})

// segment
const segmentBtn = document.getElementById('segments');
const segmentBody = document.getElementById('segments-data');
const segmentChevron = document.getElementById('segment-chevron')

let segmentBtnCounter = 0
segmentBtn.addEventListener('click', () => {
  segmentBtnCounter++;
  if (segmentBtnCounter % 2 == 0) {
    segmentBody.style.display = 'none';
    segmentChevron.classList.remove("rotate")
  } else {
    segmentBody.style.display = 'block';
    segmentChevron.classList.add("rotate")
  }
})

// categories
const categoryBtn = document.getElementById('categories');
const categoryBody = document.getElementById('categories-data');
const categoryChevron = document.getElementById('category-chevron')

let categoryBtnCounter = 0
categoryBtn.addEventListener('click', () => {
  categoryBtnCounter++;
  if (categoryBtnCounter % 2 == 0) {
    categoryBody.style.display = 'none';
    categoryChevron.classList.remove("rotate")
  } else {
    categoryBody.style.display = 'block';
    categoryChevron.classList.add("rotate")
  }
})


// filter hide btn
window.onresize = () => {
  if (window.innerWidth < 992) {
    const filterBtn = document.getElementById('filter-hide-btn');
    const filterBody = document.getElementById('hiding-filter');
    const filterChevron = document.getElementById('filter-hide-chevron');

    let filterBtnCounter = 0;

    filterBtn.addEventListener('click', () => {
      filterBtnCounter++;
      if (filterBtnCounter % 2 == 0) {
        filterBody.style.display = 'none';
        filterChevron.classList.remove("rotate")
      } else {
        filterBody.style.display = 'block';
        filterChevron.classList.add("rotate")
      }
    })
  }
}

if (window.innerWidth < 992) {
  const filterBtn = document.getElementById('filter-hide-btn');
  const filterBody = document.getElementById('hiding-filter');
  const filterChevron = document.getElementById('filter-hide-chevron');

  let filterBtnCounter = 0;

  filterBtn.addEventListener('click', () => {
    filterBtnCounter++;
    if (filterBtnCounter % 2 == 0) {
      filterBody.style.display = 'none';
      filterChevron.classList.remove("rotate")
    } else {
      filterBody.style.display = 'block';
      filterChevron.classList.add("rotate")
    }
  })
}



// Add new address

const addNewBtn = document.querySelector(".add-new-address");


function showFormShipping(){
  document.getElementById("shipping-form").style.display = "grid";
  document.getElementById("multiple-address-shipping").style.display = "none";
}

function addFormBilling(){
  document.getElementById("billing-form").style.display = "grid";
  document.getElementById("multiple-address-billing").style.display = "none";
  document.getElementById("add-header-billing").style.display = "block";
  document.getElementById("normal-header-billing").style.display = "none";
}

function editFormBilling(){
  document.getElementById("billing-form").style.display = "grid";
  document.getElementById("multiple-address-billing").style.display = "none";
  document.getElementById("add-header-billing").style.display = "none";
  document.getElementById("normal-header-billing").style.display = "none";
  document.getElementById("edit-header-billing").style.display = "block";
}
