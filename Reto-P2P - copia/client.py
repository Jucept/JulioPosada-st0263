import hello_pb2_grpc
import hello_pb2
import time
import grpc

def get_client_stream_requests():
    while True:
        name = input("Send a message: ")

        if name == "":
            break

        hello_request = hello_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        print("1. OnlyResponse - Unary")
        print("2. ServerStreaming - Server Side Streaming")
        print("3. ClientStreaming - Client Side Streaming")
        print("4. BidirectionalStreaming - Both Streaming")
        rpc_call = input("Which rpc call would you like to make: ")

        if rpc_call == "1":
            hello_request = hello_pb2.HelloRequest(greeting = "Hello", name = "Telemática")
            hello_reply = stub.OnlyResponse(hello_request)
            print("Unary Response Received:")
            print(hello_reply)
        elif rpc_call == "2":
            hello_request = hello_pb2.HelloRequest(greeting = "Hello", name = "Telemática")
            hello_replies = stub.ServerStreaming(hello_request)

            for hello_reply in hello_replies:
                print("ServerStreaming Response Received:")
                print(hello_reply)
                
        elif rpc_call == "3":
            delayed_reply = stub.ClientStreaming(get_client_stream_requests())

            print("ClientStreaming Response Received:")
            print(delayed_reply)

        elif rpc_call == "4":
            responses = stub.BidirectionalStreaming(get_client_stream_requests())

            for response in responses:
                print("BidirectionalStreaming Response Received: ")
                print(response)

if __name__ == "__main__":
    run()