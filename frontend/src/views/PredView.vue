<!-- eslint-disable -->
<template>
  <div class="page-container">
    <h1> Your Crohn's Disease Genetic Score </h1>
    <p> Use our 
      <router-link to="/our-research" class="link"> Neural Network </router-link> 
      to predict your Genetic Risk of developing Crohn's Disease
    </p>
    <h4 v-if="!file_uploaded"> Upload your file here: </h4>
    <h4 v-else-if="file_uploaded"> Your Results: </h4>
      <div class="drop-area"  v-if="!this.file_uploaded"
          @dragover="dragover"
          @dragleave="dragleave"
          @drop="drop">
            <input class="hidden" name="file" id="fileInput" ref="file" type="file" @change="uploadFile"/>
            <label for="fileInput" class="drop-instructions">
              <div v-if="isDragging"> Drop file here: </div>
              <div v-else> Drop file here or <u>click to upload</u>. </div>
            </label>
            <div v-if="this.file && !this.file_uploaded" >
                <div class="file-preview" >
                    <div>  <p> {{ this.file.name }} </p> </div>
                </div>
            </div>
            <button class="btn" @click="postToBackend" v-if="this.file && !this.file_uploaded" > Upload </button>
        </div>
    <div v-if="!file_uploaded">
    <p> Or try our services with <button class="btn" @click="testRun" style="height: 5vg; width: 10vw;"> TEST DATA </button></p>
       <div class="toggle-lists"> 
          <ToggleList title="Is my file in the right format?"
                      :index="0"
                      :width="25" >
                        <div class="inside-toggle-list">
                          <p> We can analyse any Genome files in <strong>Variant Call Format</strong> (VCF): 
                            </p> 
                            <img style="width: 25vw;" src="@/images/vcf_format.jpg"> 
                            <p> We accept gzipped versions of .vcf files (<strong>.vcf.gz</strong>) and <strong>.txt</strong> files. </p>
                        </div>
                    </ToggleList>
          <ToggleList title="What happens to my data?"
                    :index="1"
                    :width="25">
                      <div class="inside-toggle-list">
                        <p> We <strong>do not store long term</strong> any file uploaded to the system.
                          <br> We are aware of the high level of sensitivity of you data and <strong>do not sore any information</strong>
                               from your files for our research. Everything you upload will be analysed strictly for your use and any trace and data
                               collected during the process will be immediately erased from our system after the completion of the analysis. 
                          <br> However, to enable a prompt analysis of lengthy and heavy files, we do require to <strong>momentarily</strong>
                               create a local copy of your file. 
                        </p>
                      </div>
                  </ToggleList>
       </div>
    </div>
    <AlertPopup v-if="is_waiting" class="alert" type="loading"/>
    <AlertPopup v-if="show_alert" class="alert" @close="closeAlert" type="alert"/>
    <ResultTab v-if="file_uploaded && !show_alert" class="result-tab" :score="this.disease_result" :snp_list="this.user_mutations"/>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import ToggleList from '@/components/ToggleList.vue';
import ResultTab from '@/components/ResultTab.vue';
import AlertPopup from '@/components/AlertPopup.vue';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:5000/pred', 
  headers: { 'Content-Type': 'multipart/form-data' }
});


export default {
  name: "PredView",
  components: {
    ToggleList,
    ResultTab,
    AlertPopup,
  },
  data() {
      return {
        is_waiting: false,
        isDragging: false,
        file: undefined,
        file_uploaded: false,
        disease_result: [],
        user_mutations: [],
        show_alert: false
        };
    },
    methods: {
      async postToBackend() {
        try {
          const formData = new FormData();
          formData.append('file', this.file); 
          this.is_waiting = true;
          const response = await axiosInstance.post('http://127.0.0.1:5000/pred', formData);
          if (response.data.status == -1) {
              this.is_waiting = false;
              console.log(response.data.result);
              console.log('File not readable.');
              // POPUP ERROR 
              this.show_alert = true;
              this.file_uploaded = false;
              this.file = undefined;
          } 
          else{
              this.is_waiting = false;
              console.log('File uploaded successfully.');
              this.file_uploaded = true;
              console.log(response.data.status);
              this.disease_result[0] = (response.data.result);
              this.disease_result[1] = (response.data.prs);
              this.user_mutations = (response.data.user_snps);
          }         
        } catch (error) {
          console.error('Error uploading data.', error);
          this.file = undefined;
          this.file_uploaded = false;
        }
      },

      async testRun() {
        try {
          this.is_waiting = true;
          const response = await axios.get('http://127.0.0.1:5000/pred-testfile');
          if (response.data.status == -1) {
              this.is_waiting = false;
              console.log(response.data.result);
              console.log('File not readable.');
              // POPUP ERROR 
              this.show_alert = true;
              this.file_uploaded = false;
              this.file = undefined;
          } 
          else{
              this.is_waiting = false;
              console.log('File uploaded successfully.');
              this.file_uploaded = true;
              console.log(response.data.status);
              this.disease_result[0] = (response.data.result);
              this.disease_result[1] = (response.data.prs);
              this.user_mutations = (response.data.user_snps);
          }         
        } catch (error) {
          console.error('Error uploading data.', error);
          this.file = undefined;
          this.file_uploaded = false;
        }
      },

      uploadFile(event) {
        this.file = event.target.files[0];
      },
      
      dragover(e) {
        e.preventDefault();
        this.isDragging = true;
      },
      
      dragleave() {
        this.isDragging = false;
      },

      drop(event) {
        event.preventDefault();
        this.isDragging = false;
        this.file = event.dataTransfer.files[0];
      },
      closeAlert() {
        this.show_alert = false;
      },
    },
}
  </script>

<style scoped>
.page-container {
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  align-items: center;
  margin-bottom: 2vh;
  padding-top: 2vh;
  height: 100%;
  background-color: rgb(244, 244, 245, 0.5);
}

h4 {
  margin: 2vh 0 1vh 0;
  font-size: 20px;
}

a, u{
  color: rgba(125, 33, 103);
  font-weight: 500;
  font-style: italic;
  text-decoration: none;
  cursor: pointer;
}

.drop-area {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
  
  margin: 0.8rem;
  padding: 1rem 2rem 1rem 2rem;
  border-radius: 50px;
  height: 25vh;
  width: 60vw;

  background: rgba(125, 33, 103, 0.03);
  border: 3px dotted rgba(125, 33, 103, 0.1);
  box-shadow: 2px 2px 2px 2px rgba(205, 204, 204, 0.3);
}

#fileInput, .drop-instructions {
  color: rgb(72, 71, 73);
  align-self: center;
  padding: auto;
  margin: auto;
  font-size: 15px;
  cursor: pointer;
}

.hidden {
  opacity: 0;
  overflow: hidden;
  position: absolute;
  width: 1px;
  height: 1px;
}

.file-preview {
  display: flex;
  border: 1px solid rgba(125, 33, 103, 1);
  background-color: #fff;
  border-radius: 8px;
  padding: 0px 20px 0px 20px;
  margin-left: 5px;
}

.results-tab {
  margin: 20px;
}

.toggle-lists {
  display: flex;
  gap: 0.1vw;
  place-items: flex-start;
  align-content: center;
}

.toggle-lists p{
  text-align: justify;
}

</style>