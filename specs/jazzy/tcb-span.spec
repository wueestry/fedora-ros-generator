# Meta Package
Name:           ros-jazzy-tcb-span
Version:        1.0.2
Release:        1%{?dist}
License:        Boost Software License
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tcb_span and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tcb_span
Requires:       ros2-jazzy-tcb_span-devel

Obsoletes: ros-jazzy-tcb-span < 1.0.2-1

%description
Implementation of C++20's std::span

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.2-1
- Update to latest release
