# Meta Package
Name:           ros-humble-quality-of-service-demo-py
Version:        0.20.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-quality_of_service_demo_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-quality_of_service_demo_py
Requires:       ros2-humble-quality_of_service_demo_py-devel

Obsoletes: ros-humble-quality-of-service-demo-py < 0.20.5-1

%description
Python Demo applications for Quality of Service features

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.5-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.4-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- Initial humble build
