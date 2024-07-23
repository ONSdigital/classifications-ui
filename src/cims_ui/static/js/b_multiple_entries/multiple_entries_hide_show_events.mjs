
const radioButtonSIC = document.querySelector('#SIC');
const radioButtonSOC = document.querySelector('#SOC');
const textBoxBizDesc = document.querySelector('#business_desc_col_name');
const textBoxJobTitle = document.querySelector('#job_title_col_name');
const textBoxQual = document.querySelector('#qualification_col_name');
const textBoxBizDescParent = textBoxBizDesc.parentNode;
const textBoxJobTitleParent = textBoxJobTitle.parentNode;
const textBoxQualParent = textBoxQual.parentNode;

function disableAllTextInputs() {
  textBoxBizDescParent.style.display = 'none';
  textBoxJobTitleParent.style.display = 'none';
  textBoxQualParent.style.display = 'none';
  }

window.addEventListener("load", disableAllTextInputs);

radioButtonSIC.addEventListener('click', () => {
            // Find the text boxes we want to disable
            textBoxJobTitle.disabled = true;
            textBoxQual.disabled = true;
            textBoxJobTitle.value = "";
            textBoxQual.value = "";
            textBoxJobTitleParent.style.display = 'none';
            textBoxQualParent.style.display = 'none';
           // Find boxes to enable
            textBoxBizDesc.disabled = false;
            textBoxBizDescParent.style.display = 'block';
        });

radioButtonSOC.addEventListener('click', () => {
           // Find boxes to enable
            textBoxBizDesc.disabled = false;
            textBoxJobTitle.disabled = false;
            textBoxQual.disabled = false;
            textBoxBizDescParent.style.display = 'block';
            textBoxJobTitleParent.style.display = 'block';
            textBoxQualParent.style.display = 'block';
        });
