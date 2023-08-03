from pytm import TM, Server, Dataflow, Boundary # This comment # type: ignore

tm = TM("My Threat Model")
tm.description = "A simple"

boundary = Boundary("My Boundary")

web = Server("Web Server")
web.inBoundary = boundary

db = Server("Database Server")
db.inBoundary = boundary

dataflow = Dataflow(web, db, "Data Flow")
dataflow.protocol = "HTTPS"

tm.process()
