# Meta Package
Name:           ros-jazzy-quality-of-service-demo-cpp
Version:        0.33.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-quality_of_service_demo_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-quality_of_service_demo_cpp
Requires:       ros2-jazzy-quality_of_service_demo_cpp-devel

Obsoletes: ros-jazzy-quality-of-service-demo-cpp < 0.33.5-1

%description
C++ Demo applications for Quality of Service features

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.5-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.2-1
- Update to latest release
