from concurrent import futures   #Set the number of workers on my server
import time
import grpc
import hello_pb2
import hello_pb2_grpc

class GreeterServicer(hello_pb2_grpc.GreeterServicer):
    def OnlyResponse(self, request, context):
        print("Unary Request Made:")
        print(request)
        hello_reply = hello_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"
        return hello_reply

    
    def ServerStreaming(self, request, context):
        print("Server Request Made:")
        print(request)

        for i in range(5):
            hello_reply = hello_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name} {i + 1}" # i + 1 para poder mostrar una cuenta de los mensajes
            yield hello_reply # Se usa yield en lugar de return porque es mejor para server streaming que return
            time.sleep(2) # Para no recibir todas las respuestas de una sola vez
        
    
    def ClientStreaming(self, request_iterator, context):
        delayed_reply = hello_pb2.DelayedReply()
        
        for request in request_iterator:
            print("Client Request Made:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply
    
    def BidirectionalStreaming(self, request_iterator, context):
        for request in request_iterator:
            print("Bidirectional Request Made:")
            print(request)

            hello_reply = hello_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name}"

            yield hello_reply
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    print("Server Started")
    print("Waiting for RPC call...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
