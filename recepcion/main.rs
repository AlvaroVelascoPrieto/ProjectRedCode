use std::net::UdpSocket;

fn main() -> std::io::Result<()> {
    match simple_redis::create("redis://127.0.0.1:6379/") {
        Ok(mut client) => {
            println!("Created Redis Client");

            let ids: [&str; 48] = ["0310","0090", "00f0", "00f1", "00f2", "00a2", "0001", "0311", "01cf", 
            "02cf", "01ce", "02ce", "024f", "034f", "024e", "034e", "028f", "038f", "028e", "038e", "020e", 
            "040e", "020f", "040f", "0122", "0181", "0101", "0102", "0103", "0104", "0105", "0106", "0107", 
            "0108", "0109", "010a", "010b", "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", 
            "1109", "110a", "110b"]; //Predefined ids to populate db
            let socket = UdpSocket::bind("127.0.0.1:3002")?;

            //Populate db with 0s
            for id in ids.into_iter() {
                println!("Populated {}", id);
                match client.set(id, "0000000000000000") {
                    Err(error) => println!("Unable to set value in Redis: {}", error),
                    _ => println!("Value set in Redis"),
                };
            
            }

            match client.set("my_key", "my_value") {
                Err(error) => println!("Unable to set value in Redis: {}", error),
                _ => println!("Value set in Redis"),
            };

            match client.get_string("my_key") {
                Ok(value) => println!("Read value from Redis: {}", value),
                Err(error) => println!("Unable to get value from Redis: {}", error),
            };

        }
        Err(error) => println!("Unable to create Redis client: {}", error),
    }

    loop {
        let mut buf = [0; 10];
        let result = socket.recv_from(&mut buf).expect("Didn't receive data");;
        match result {
            Ok((amt, src)) => {
              data = Vec::from(&buf[0..amt]);
            },
            Err(err) => println!("Read error: {}", err)
        }
        let id = to_string(&data[1..=4])
        let data to_string(&data[4..])
        match client.set(id, data) {
            Err(error) => println!("Unable to set value in Redis: {}", error),
            _ => println!("Value set in Redis"),
        };        
    }
}
