<template>
  <div class="modtype">
    <b-card
      overlay
      img-src="https://gilmourlance.org/wp-content/uploads/2016/03/11.jpg"
      img-alt="Card Image"
      text-variant="white"
      title="Module Type"
      title-tag="h1"
      img-height="350px"
    >
      <b-card-text>
        Discover modules based on their module types.</br>
        Find out what others chose for their Programme Electives, or/ and find out more about popular GE mods.
      </b-card-text>
    </b-card>
    <b-container fluid class="content">

      </br></br>
      <ModuleTypeDataTable/>
      </br></br>
    </b-container>
    <Footer/>
  </div>
</template>

<script>
  import Footer from "@/components/Footer.vue";
  import ModuleTypeDataTable from "@/components/ModuleTypeDataTable.vue";
  export default {
    name: "modtype",
    components: {
      ModuleTypeDataTable,
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
