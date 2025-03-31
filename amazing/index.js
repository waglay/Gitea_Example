import express from "express";


const app = express();
const PORT = 5000; // Serve index.html on this port
const INSTANCE_ID = process.env.INSTANCE_ID || "1";

// ✅ Serve the index.html file
app.get("/", (req, res) => {
    res.send({message:`${INSTANCE_ID}`});
    console.log("the instance is: ", `${INSTANCE_ID}`);
});

// ✅ Start Express server
app.listen(PORT, () => {
    console.log(`🌍 Page server running at: http://localhost:${PORT}`);
});
