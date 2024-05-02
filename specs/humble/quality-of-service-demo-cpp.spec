# Meta Package
Name:           ros-humble-quality-of-service-demo-cpp
Version:        0.20.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-quality_of_service_demo_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-quality_of_service_demo_cpp
Requires:       ros2-humble-quality_of_service_demo_cpp-devel

Obsoletes: ros-humble-quality-of-service-demo-cpp < 0.20.3-1

%description
C++ Demo applications for Quality of Service features

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- Initial humble build
