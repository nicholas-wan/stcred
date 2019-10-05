<template>
  <div class="industry_page">
    <b-card
      overlay
      img-src="https://wonderfulengineering.com/wp-content/uploads/2016/01/singapore-wallpaper-3.jpg"
      img-alt="Card Image"
      text-variant="white"
      title="Industry"
      title-tag="h1"
      img-height="350px"
    >
      <b-card-text>
        Discover modules recently employed graduates took while they were studying.</br>
        This information can serve as a useful guideline of skills and knowledge that would be helpful for a certain industry.
      </b-card-text>
    </b-card>
    <b-container fluid class="content">
      </br></br>
      <IndustryDataTable/>
      </br></br>
    </b-container>
    <Footer/>
  </div>
</template>

<script>
  import Footer from "@/components/Footer.vue";
  import IndustryDataTable from "@/components/IndustryDataTable.vue";
  export default {
    name: "industry",
    components: {
      IndustryDataTable,
      Footer
    }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.titlePosition {
  color: #003d7c;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: "bold";
  font-size: 56px;
  width: 100%;
  text-align: center;
  margin-top: 50px;
  padding-bottom: 0px;
}

.moduleTitle {
  color: #003d7c;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: "bold";
  font-size: 56px;
  width: 100%;
  text-align: center;
  margin-top: 0px;
  margin-left: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
}

.shiftLeft {
  padding-right: 15px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

/* ---------CSS for banner------------- */
.card-img{
  object-fit:cover;
  object-position:center;
  filter: brightness(40%);
}
h1{
  color:white;
  margin-top:7rem;
  font-size:4rem;
}
.cart-text{
  font-size:2rem;
}

</style>
