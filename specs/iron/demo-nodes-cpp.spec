# Meta Package
Name:           ros-iron-demo-nodes-cpp
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-demo_nodes_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-demo_nodes_cpp
Requires:       ros2-iron-demo_nodes_cpp-devel

Obsoletes: ros-iron-demo-nodes-cpp < 0.27.1-1

%description
C++ nodes which were previously in the ros2/examples repository but
are now just used for demo purposes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
