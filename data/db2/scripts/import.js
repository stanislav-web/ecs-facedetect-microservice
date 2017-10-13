db.createUser({
    user: 'administrator',
    pwd: 'password',
    roles: [ {
        role: 'readWrite',
        db: 'storage'
    }]
});
db.createCollection('images');
db.access.ensureIndex({email:1},{unique:true});