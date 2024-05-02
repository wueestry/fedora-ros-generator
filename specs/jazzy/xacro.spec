# Meta Package
Name:           ros-jazzy-xacro
Version:        2.0.11
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/xacro
Summary:        Meta package for ros2-jazzy-xacro and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-xacro
Requires:       ros2-jazzy-xacro-devel

Obsoletes: ros-jazzy-xacro < 2.0.11-1

%description
Xacro (XML Macros) Xacro is an XML macro language. With xacro, you can
construct shorter and more readable XML files by using macros that
expand to larger XML expressions.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.11-1
- Update to latest release
