extern crate redis;
use redis::Commands;
use std::net::UdpSocket;

fn main() -> std::io::Result<()> {
    {
        let ids: [&str; 48] = ["0310","0090", "00f0", "00f1", "00f2", "00a2", "0001", "0311", "01cf", 
        "02cf", "01ce", "02ce", "024f", "034f", "024e", "034e", "028f", "038f", "028e", "038e", "020e", 
        "040e", "020f", "040f", "0122", "0181", "0101", "0102", "0103", "0104", "0105", "0106", "0107", 
        "0108", "0109", "010a", "010b", "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", 
        "1109", "110a", "110b"]; //Predefined ids to populate db
        let mut redisConn = connect();
        let socket = UdpSocket::bind("127.0.0.1:34254")?;

        //Populate db with 0s
        for id in ids.into_iter() {
            println!("Populated {}", id);
            let _: () = redis::cmd("SET")
                .arg(id)
                .arg("0000000000000000")
                .query(&mut redisConn)
                .expect(&format!("failed to execute SET for {}", id));
        }
        
        //Main loop
        loop{
            //UDP reception from buffer
            let mut buf = [0; 10];
            let (number_of_bytes, src_addr) = socket.recv_from(&mut buf)
                                                    .expect("Didn't receive data");
            let filled_buf = &mut buf[..number_of_bytes];
            
            //Message treatment
            let id = &filled_buf[0..4].escape_ascii()
                                        .to_string();
            let data = format!("{:0<8}", &filled_buf[4..number_of_bytes].escape_ascii().to_string().as_str());
            let _: () = redis::cmd("SET")
                .arg(id)
                .arg(data)
                .query(&mut redisConn)
                .expect(&format!("failed to execute SET for {}", id));
            let retreivedData: String = redis::cmd("GET")
                .arg(id)
                .query(&mut redisConn)
                .expect(&format!("failed to execute GET for {}", id));
            println!("value for {} = {}", id, retreivedData); 
        }
    }
    Ok(())
}

fn connect() -> redis::Connection {
    let redis_conn_url = "redis://redis:6379/";
    redis::Client::open(redis_conn_url)
        .expect("Invalid connection URL")
        .get_connection()
        .expect("failed to connect to Redis")
}