# Meta Package
Name:           ros-iron-intra-process-demo
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-intra_process_demo and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-intra_process_demo
Requires:       ros2-iron-intra_process_demo-devel

Obsoletes: ros-iron-intra-process-demo < 0.27.1-1

%description
Demonstrations of intra process communication.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
