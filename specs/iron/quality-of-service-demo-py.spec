# Meta Package
Name:           ros-iron-quality-of-service-demo-py
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-quality_of_service_demo_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-quality_of_service_demo_py
Requires:       ros2-iron-quality_of_service_demo_py-devel

Obsoletes: ros-iron-quality-of-service-demo-py < 0.27.1-1

%description
Python Demo applications for Quality of Service features

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
