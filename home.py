from pytm import TM, Server, Dataflow, Boundary

tm = TM("My Threat Model")
tm.description = "A simple threat model example"

boundary = Boundary("My Boundary")

web = Server("Web Server")
web.inBoundary = boundary

db = Server("Database Server")
db.inBoundary = boundary

dataflow = Dataflow(web, db, "Data Flow")
dataflow.protocol = "HTTPS"

tm.process()
