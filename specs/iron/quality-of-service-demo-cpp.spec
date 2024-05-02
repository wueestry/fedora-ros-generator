# Meta Package
Name:           ros-iron-quality-of-service-demo-cpp
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-quality_of_service_demo_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-quality_of_service_demo_cpp
Requires:       ros2-iron-quality_of_service_demo_cpp-devel

Obsoletes: ros-iron-quality-of-service-demo-cpp < 0.27.1-1

%description
C++ Demo applications for Quality of Service features

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
