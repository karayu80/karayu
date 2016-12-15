#include <cstdio>
#include <ctime>
#include <iostream>
#include <string>
#include <boost/asio.hpp>
#include <ctime>
#include <iostream>
#include <string>
#include <boost/bind.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/enable_shared_from_this.hpp>

#include <boost/date_time/posix_time/posix_time.hpp>

using boost::asio::ip::tcp;

// �޼����� �����.
std::string make_daytime_string()
{
	using namespace std; // For time_t, time and ctime;
	time_t now = time(0);
	return ctime(&now);	// ctime_s ����. �����ϱ� �׳� ���� �Ѿ����
}

class CTCP_Connection : public boost::enable_shared_from_this<CTCP_Connection>
{
private:
	tcp::socket m_Socket;
	std::string m_sMessage;

	CTCP_Connection(boost::asio::io_service& io_service) : m_Socket(io_service) // m_Socket �ʱ�ȭ
	{
	}

	// �Ⱦ��ϱ� �����ϰ� ����
	void handle_write(const boost::system::error_code& /*error*/, size_t /*bytes_transferred*/)
	{
	}

public:
	typedef boost::shared_ptr<CTCP_Connection> pointer;

	static pointer create(boost::asio::io_service& io_service)
	{
		return pointer(new CTCP_Connection(io_service));
	}

	tcp::socket& socket()
	{
		return m_Socket;
	}

	void start()
	{
		m_sMessage = make_daytime_string();

		// ���������� boost::asio::async_write (boost::asio::error::eof ����) �� ������
		// async_write_some, async_send �� ����� ���̴�
		// error, bytes_tran �κ��� ������� �ʾƵ� �ȴ�
		boost::asio::async_write(m_Socket, boost::asio::buffer(m_sMessage),
			boost::bind(&CTCP_Connection::handle_write, shared_from_this(),
				boost::asio::placeholders::error,
				boost::asio::placeholders::bytes_transferred));
	}
};

class CTCP_Server
{
private:
	tcp::acceptor m_Acceptor;

	void start_accept()
	{
		CTCP_Connection::pointer new_connection =
			CTCP_Connection::create(m_Acceptor.get_io_service());

		m_Acceptor.async_accept(new_connection->socket(),
			boost::bind(&CTCP_Server::handle_accept, this, new_connection,
				boost::asio::placeholders::error));
	}

	void handle_accept(CTCP_Connection::pointer new_connection, const boost::system::error_code& error)
	{
		if (!error)
		{
			new_connection->start();
			start_accept();
		}
	}

public:
	CTCP_Server(boost::asio::io_service& io_service) : m_Acceptor(io_service, tcp::endpoint(tcp::v4(), 13))
	{
		start_accept();
	}
};


int main()
{
    printf("hello from dddd!\n");
	try
	{
		boost::asio::io_service io_service;	// asio ��� ������ �־�� �Ѵ�

		CTCP_Server server(io_service);
		io_service.run();
	}
	catch (std::exception& e)
	{
		std::cerr << e.what() << std::endl;
	}

	return 0;
}