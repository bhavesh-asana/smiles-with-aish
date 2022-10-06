package com.smiles;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Filters;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import org.bson.Document;
import org.bson.types.ObjectId;

import java.util.Objects;

public class CalcInfoImpl extends CalcInfoServiceGrpc.CalcInfoServiceImplBase {

    /* >>>>>>>>   Connecting to MongoDB (the BSON document)  >>>>>>>>>>>
     *  MongoDB Hierarchy: Database -> Collection -> Record
     *  Connecting port: localhost:27017 (default port)
     *  Database name: SMILESDataModels
     *  Collection name: InfoDataModel
     * >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*/
    private final MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017");
    private final MongoDatabase mongoDatabase = mongoClient.getDatabase("smilesDB");
    private final MongoCollection<org.bson.Document> mongoCollection = mongoDatabase.getCollection("calcInfo");
    /* <<<<<<<<<<<  End of MongoDB connection parameters  <<<<<<<<<<<<<*/

    // Buildina document method.
    private CalcInfo documentToCalcInfo(Document document) {
        return CalcInfo.newBuilder()
                .setSmiles(document.getString("smiles"))
                .setCalcinfoId(String.valueOf(document.getObjectId("_id")))
                .setNbasis(Long.parseLong(Objects.equals(String.valueOf(document.getString("nbasis")), "") ? "0" : ""))
                .setNmo(Long.parseLong(String.valueOf(document.getLong("nmo"))))
                .setNalpha(document.getLong("nalpha"))
                .setNbeta(document.getLong("nbeta"))
                .setNatom(document.getLong("natom"))
                .setEnergy(document.getDouble("energy"))
                .build();
    }

    //    Implementing the CREATE operation method
    //    ✅ Built Success
    @Override
    public void createCalcinfo(CreateInfoRequest request, StreamObserver<CreateInfoResponse> responseObserver) {

        System.out.println(" \n\n -----------  INSERT OPERATION ---------- ");
        System.out.println("Received request for indexing a data to MongoDB");
        CalcInfo calcInfo = request.getCalcInfo();

        System.out.println("Running INSERT operation");
        // calcinfo_id is not passed in CREATE method
        Document document = new Document("calcinfo_id", calcInfo.getCalcinfoId())
                .append("smiles", calcInfo.getSmiles())
                .append("nbasis", calcInfo.getNbasis())
                .append("nmo", calcInfo.getNmo())
                .append("nalpha", calcInfo.getNalpha())
                .append("nbeta", calcInfo.getNbeta())
                .append("natom", calcInfo.getNatom())
                .append("energy", calcInfo.getEnergy());

        // Command to insert a document into a database -> collection
        mongoCollection.insertOne(document);
        System.out.println("Inserted an entity to mongoDB record");

        // Get the ID from MongoDb
        String id = document.getObjectId("_id").toString();
        System.out.println("Entity ID: " + id);
        System.out.println("----------------------------------------");

        // Create MongoResponse
        CreateInfoResponse infoResponse = CreateInfoResponse.newBuilder().setCalcInfo(
                        calcInfo.toBuilder().setCalcinfoId(id).build()
                )
                .build();
        responseObserver.onNext(infoResponse);
        responseObserver.onCompleted();
    }


    //    Implementing the READ/GET operation method
    //    ✅ Built Success
    @Override
    public void readCalcInfo(ReadInfoRequest request, StreamObserver<ReadInfoResponse> responseObserver) {

        System.out.println("Received request for Fetching a Blog from MongoDB.");

        Document fetchedDocFromMongo =
                mongoCollection.find(Filters.eq("_id", new ObjectId(request.getId()))).first();

        if (fetchedDocFromMongo == null) {
            responseObserver
                    .onError(Status.NOT_FOUND.withDescription("No blog exists with this Id.").asRuntimeException());
        } else {
            ReadInfoResponse fetchedBlogResponse = ReadInfoResponse.newBuilder()
                    .setCalcInfo(CalcInfo.newBuilder()
                            .setSmiles(fetchedDocFromMongo.getString("smiles"))
                            .setCalcinfoId(String.valueOf(fetchedDocFromMongo.getObjectId("_id")))
                            .setNbasis(Long.parseLong(String.valueOf(fetchedDocFromMongo.getLong("nbasis"))))
                            .setNmo(Long.parseLong(String.valueOf(fetchedDocFromMongo.getLong("nmo"))))
                            .setNalpha(fetchedDocFromMongo.getLong("nalpha"))
                            .setNbeta(fetchedDocFromMongo.getLong("nbeta"))
                            .setNatom(fetchedDocFromMongo.getLong("natom"))
                            .setEnergy(fetchedDocFromMongo.getDouble("energy"))
                            .build())
                    .build();

            responseObserver.onNext(fetchedBlogResponse);
        }
        responseObserver.onCompleted();
    }

    //    Implementing the LIST operation method
    //    ✅ Built Success
    @Override
    public void listCalcInfo(ListInfoRequest request, StreamObserver<ListInfoResponse> responseObserver) {
        System.out.println(" \n\n -----------  LIST OPERATION ---------- ");
        System.out.println("Received a request to LIST the Info data.");

        // Searching for the data from mongo collection (iteration: document by document)
        mongoCollection.find().iterator().forEachRemaining(document -> responseObserver.onNext(
                ListInfoResponse.newBuilder()
                        .setCalcInfo(documentToCalcInfo(document)).build()
        ));

        System.out.println("Successfully displayed the Info Data from Mongo Collection");
        System.out.println("----------------------------------------");
        responseObserver.onCompleted();
    }


    @Override
    public void updateCalcInfo(UpdateInfoRequest request, StreamObserver<UpdateInfoResponse> responseObserver) {
        super.updateCalcInfo(request, responseObserver);
    }

    @Override
    public void deleteCalcInfo(DeleteInfoRequest request, StreamObserver<DeleteInfoResponse> responseObserver) {
        super.deleteCalcInfo(request, responseObserver);
    }


}